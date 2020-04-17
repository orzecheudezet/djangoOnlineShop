# Checkout process

1. Cart => Checkout views
  ?
  - Login or Enter an Email(as Guest)
  - Shipping Adress
  - Billing Info
    - Billing Adress
    - Credit Card / Payment

2. Billing App/Component
  - Billing Profile
    - User or Email (Guest Email)
    - Generate payment processor token (Stripe or Braintree)

3. Orders / Invoices Component
  - Connecting the Billing Profile
  - Shipping / Billing Address
  - Cart
  - Status == Shiped? Cancelled?
