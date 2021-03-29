import { EcommerceOrderState } from './ecommerce-order-state';
import { EcommerceOrder } from './ecommerce-order';
import { OrderPending } from './order-pending';
import { OrderRejected } from './order-rejected';

export class OrderApproved implements EcommerceOrderState {
  private name = 'OrderApproved';

  constructor(private order: EcommerceOrder) {}

  getName(): string {
    return this.name;
  }

  approvePayment(): void {
    console.log('O pedido já está no estado pagamento aprovado.');
  }

  rejectPayment(): void {
    this.order.setState(new OrderRejected(this.order));
  }

  waitPayment(): void {
    this.order.setState(new OrderPending(this.order));
  }

  shipOrder(): void {
    console.log('Enviando pedido para o cliente...');
  }
}