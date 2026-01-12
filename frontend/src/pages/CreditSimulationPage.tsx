import { useState } from "react";
import { CashflowTable } from "../components/CashflowTable";
import { SimulationForm } from "../components/SimulationForm";
import { toPayment, type PaymentModel } from "../domain";
import { CreditSimulatorService } from "../api";

export function CreditSimulationPage() {
  const service = new CreditSimulatorService();

  const [installments, setInstallments] = useState<PaymentModel[]>([]);

  const [amount, setAmount] = useState<string>(() => {
    return localStorage.getItem("amount") || "";
  });

  const [rate, setRate] = useState<string>(() => {
    return localStorage.getItem("rate") || "";
  });

  const [term, setTerm] = useState<string>(() => {
    return localStorage.getItem("term") || "";
  });

  const handleChangeAmount = (value: number) => {
    setAmount(value.toString());
    localStorage.setItem("amount", value.toString());
    setInstallments([]);
  };

  const handleChangeRate = (value: number) => {
    setRate(value.toString());
    localStorage.setItem("rate", value.toString());
  };

  const handleChangeTerm = (value: number) => {
    setTerm(value.toString());
    localStorage.setItem("term", value.toString());
  };

  const handleSubmit = async () => {
    const dto = await service.Create({
      credit_amount: Number(amount),
      annual_rate: Number(rate),
      term: Number(term),
    });

    if (!dto.ok) {
      setInstallments([]);
      return;
    }
    const payments = dto.resultData?.installments.map(toPayment) ?? [];
    setInstallments(payments);
  };

  return (
    <>
      <SimulationForm
        amount={amount}
        rate={rate}
        months={term}
        onChangeAmount={handleChangeAmount}
        onChangeRate={handleChangeRate}
        onChangeMonths={handleChangeTerm}
        onSubmit={handleSubmit}
      ></SimulationForm>
      <CashflowTable cashflow={installments}></CashflowTable>
    </>
  );
}
