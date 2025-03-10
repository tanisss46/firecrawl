# Stripe Connector for Shopware 6 User Guide

## Learn how to use the Stripe Connector for Shopware 6.

## Payment information at order level

On the order, the **Payments** tab displays the following details about your
Stripe payment:

- **Description**: Shows the customer email address, Customer ID and Order ID.
- **Payment Intent Status**: Shows the order’s payment status.
- **Payment Method**: Identifies the payment instrument used to pay.
- **Payment Risk Score**: Grades the fraud risk of the payment.
- **Timeline**: The sequence of events that occurred during payment.

## Cancel a payment

You can cancel a payment when it’s uncaptured and its status is **Authorized**.

- From Shopware, change the order’s status from **Authorized** to **Cancelled**
- From the Stripe Dashboard, click the **Cancel** button inside the order.

## Refunds

You can refund any order with a `Paid` status.

- From the Shopware administration panel, select **Orders** >> **Overview** .
- Change the order’s payment status from `Paid` to `Refunded`.

Shopware doesn’t support partial refunds. Choosing either the `Refunded
(partially)` or `Refunded` status generates a full refund.