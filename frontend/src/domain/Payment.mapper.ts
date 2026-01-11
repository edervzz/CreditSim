import type { PaymentSimulationDto } from "../api/CreditSimulation.dto";
import type { PaymentModel } from "./Payment.model";

export function toPayment(dto: PaymentSimulationDto): PaymentModel{
    return {
        month: dto.month,
        quota: dto.quota,
        interest: dto.interest,
        principal: dto.principal,
        outstanding: dto.outstanding
    }
}