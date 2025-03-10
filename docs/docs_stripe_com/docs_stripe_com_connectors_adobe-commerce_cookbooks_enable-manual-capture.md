# Enable manual capture

## Allow separate authorization and capture for eligible Stripe payment methods.

Stripe supports manual capture for some payment method types. You can configure
this behavior in the application settings page by setting the `Payment Action`
property of an eligible payment method to **Authorize Only**.

Typically, enabling manual capture for a newly launched payment method that
supports it requires upgrading your Stripe module. This guide instructs you how
to enable manual capture for eligible payment methods without upgrading the
Stripe module by updating the payment method helper file directly.

## Create a new module

Create a new module with the following directory structure. Replace `Vendor`
with your preferred vendor name.

```
app/code/Vendor/StripeCustomizations/
├── etc/
│ ├── module.xml
│ └── di.xml
├── Plugin/
│ └── Helper/
│ └── PaymentMethodPlugin.php
├── registration.php

```

Inside `registration.php`, register your module with Magento.

```
<?php
\Magento\Framework\Component\ComponentRegistrar::register(
 \Magento\Framework\Component\ComponentRegistrar::MODULE,
 'Vendor_StripeCustomizations',
 __DIR__
);
```

Inside `etc/module.xml`, define the module and set up dependencies to make sure
it loads after the Stripe module.

```
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
 <module name="Vendor_StripeCustomizations" setup_version="1.0.0">
 <sequence>
 <module name="StripeIntegration_Payments"/>
 </sequence>
 </module>
</config>
```

Inside `etc/di.xml`, define the following plugin:

```
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
 <type name="StripeIntegration\Payments\Helper\PaymentMethod">
 <plugin
 name="vendor_stripecustomizations_helper_paymentmethod_plugin"
 type="Vendor\StripeCustomizations\Plugin\Helper\PaymentMethodPlugin"
 sortOrder="10"
 disabled="false" />
 </type>
</config>
```

Inside `Plugin/Helper/PaymentMethodPlugin.php`, create the an `afterMethod`
interceptor:

```
<?php

namespace Vendor\Module\Plugin;

class PaymentMethodPlugin
{
 public function afterGetPaymentMethodsThatCanCaptureManually(
 \StripeIntegration\Payments\Helper\PaymentMethod $subject,
 $result
 ) {
// Modify or extend the result to include another payment method code that
supports manual capture.
 $result[] = 'new_payment_method_code';

 return $result;
 }
}
```

Enable the module:

```
php bin/magento module:enable Vendor_StripeCustomizations
php bin/magento setup:upgrade
php bin/magento cache:clean
php bin/magento cache:flush

```

## Links

-
[http://www.w3.org/2001/XMLSchema-instance](http://www.w3.org/2001/XMLSchema-instance)