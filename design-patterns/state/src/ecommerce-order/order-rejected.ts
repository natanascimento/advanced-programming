import { EcommerceOrderState } from './ecommerce-order-state';
import { EcommerceOrder } from './ecommerce-order';

export class OrderRejected implements EcommerceOrderState {
  private name = 'OrderRejected';

  constructor(private order: EcommerceOrder) {}

  getName(): string {
    return this.name;
  }

  approvePayment(): void {
    console.log('Não posso aprovar o pagamento porque o pedido foi recusado.');
  }

  rejectPayment(): void {
    console.log(
      'Não posso recusar o pagamento porque o pedido já está recusado.',
    );
  }

  waitPayment(): void {
    console.log('Não posso mover para pendente porque o pedido foi recusado.');
  }

  shipOrder(): void {
    console.log('Não posso enviar um pedido com pagamento recusado.');
  }
}