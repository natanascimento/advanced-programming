import { EcommerceOrder } from './ecommerce-order/ecommerce-order';

const order = new EcommerceOrder();
order.approvePayment();
order.waitPayment();
order.shipOrder();
order.rejectPayment();
order.approvePayment();
order.waitPayment();
order.approvePayment();
order.shipOrder();
