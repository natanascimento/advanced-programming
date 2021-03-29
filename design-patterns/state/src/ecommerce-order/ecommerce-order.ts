import { EcommerceOrderState } from './ecommerce-order-state';
import { OrderPending } from './order-pending';

export class EcommerceOrder {
  private state: EcommerceOrderState = new OrderPending(this);

  getState(): EcommerceOrderState {
    return this.state;
  }

  setState(state: EcommerceOrderState): void {
    this.state = state;
    console.log(`O estado do pedido agora é ${this.getStateName()}`);
  }

  getStateName(): string {
    return this.state.getName();
  }

  approvePayment(): void {
    this.state.approvePayment();
  }

  rejectPayment(): void {
    this.state.rejectPayment();
  }

  waitPayment(): void {
    this.state.waitPayment();
  }

  shipOrder(): void {
    this.state.shipOrder();
  }
}