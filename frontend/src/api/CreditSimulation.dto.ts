export type CreditSimulationRequestDto = {
    credit_amount: number
    annual_rate: number
    term: number
}


export type CreditSimulationResponseDto = {
    installments: [PaymentSimulationDto]
}

export type PaymentSimulationDto = {
    month: number
    quota: number
    interest: number
    principal: number
    outstanding: number
}