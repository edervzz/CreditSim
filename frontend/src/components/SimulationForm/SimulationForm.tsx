import { useRef } from "react";

interface Props {
  onSubmit?: (amount: number, rate: number, months: number) => void;
}

export function SimulationForm({ onSubmit }: Props) {
  const amountRef = useRef<HTMLInputElement>(null);
  const rateRef = useRef<HTMLInputElement>(null);
  const monthsRef = useRef<HTMLInputElement>(null);
  return (
    <div className="container" style={{ backgroundColor: "" }}>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit?.(
            Number(amountRef.current?.value) || 0,
            Number(rateRef.current?.value) || 0,
            Number(monthsRef.current?.value) || 0
          );
        }}
      >
        <div className="row align-items-center">
          <div className="col-12 col-md-3 col-xl-2">Credit Amount</div>
          <div className="col">
            <input
              className="form-control"
              type="number"
              min={0}
              step={0.01}
              ref={amountRef}
              aria-label="Credit Amount"
            />
          </div>
        </div>
        <div className="row align-items-center">
          <div className="col-12 col-md-3 col-xl-2">Interest Rate</div>
          <div className="col">
            <input
              className="form-control"
              type="number"
              min={0}
              step={0.01}
              ref={rateRef}
              aria-label="Annual Interest Rate"
            />
          </div>
        </div>
        <div className="row align-items-center">
          <div className="col-12 col-md-3 col-xl-2">Term (in months)</div>
          <div className="col">
            <input
              className="form-control"
              type="number"
              min={0}
              ref={monthsRef}
              aria-label="Term in months unit"
            />
          </div>
        </div>
        <div className="row justify-content-center pt-1">
          <div className="col text-end">
            <button type="submit" className="btn btn-primary">
              Simulate
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
