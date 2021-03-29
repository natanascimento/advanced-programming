export interface EcommerceOrderState {
    getName(): string;
    approvePayment(): void;
    rejectPayment(): void;
    waitPayment(): void;
    shipOrder(): void;
  }