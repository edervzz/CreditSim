import { useState } from "react";
import { CashflowTable } from "../components/CashflowTable";
import { SimulationForm } from "../components/SimulationForm";
import { toPayment, type PaymentModel } from "../domain";
import { CreditSimulatorService } from "../api";

export function CreditSimulation() {
  const [cashflow, setCashflow] = useState<PaymentModel[]>([]);

  const service = new CreditSimulatorService();

  const handleSubmit = async (amount: number, rate: number, months: number) => {
    const dto = await service.Create({
      credit_amount: amount,
      annual_rate: rate,
      term: months,
    });

    if (!dto.ok) {
      setCashflow([]);
      return;
    }
    const payments = dto.resultData?.cashflow.map(toPayment) ?? [];
    setCashflow(payments);
  };

  return (
    <>
      <SimulationForm onSubmit={handleSubmit}></SimulationForm>
      <CashflowTable cashflow={cashflow}></CashflowTable>
    </>
  );
}
