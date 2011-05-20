# -*- coding: utf-8 -*-

def index():
    products = db(db.product).select(orderby=db.product.sortable)
    return locals()


    return dict(message=T('Hello World'))

def user():
    return dict(form=auth())


def download():
    return response.download(request,db)

def call():
    session.forget()
    return service()

@auth.requires_login()
def cart():
    return dict(cart=session.cart)

@auth.requires_login()
def buy():
    import uuid
    invoice = str(uuid.uuid4())
    total = sum(db.product(id).price*qty for id,qty in session.cart.iteritems())
    form = SQLFORM.factory(Field('creditcard', default='44243254354367423345'),
                           Field('expiration', default='12/20012'),
                           Field('cvv', default='123'),
                           Field('total', 'double', default=total, writable=False))
    if form.accepts(request, session):
        if process(form.vars.creditcard, form.vars.expiration,
                   total,form.vars.cvv,0.0, 'invoice'):

            for key, value in session.cart.iteritems():
                db.sale.insert(buyer = auth.user.id,
                               product = key,
                               quantity = value,
                               price = db.product(key).price,
                               creditcard = form.vars.creditcard)
            session.cart.clear()
            session.flash = T('Thank you for your order')
            redirect(URL('index'))
        else:
            response.flash = T('payment rejected (please call')
    return dict(cart=session.cart, form=form)

def cart_callback():
    id = int(request.vars.id)
    if request.vars.action == 'add':
        session.cart[id]=session.cart.get(id,0)+1
    if request.vars.action == 'sub':
        session.cart[id]=max(0,session.cart.get(id,0)-1)
    return str(session.cart[id])
