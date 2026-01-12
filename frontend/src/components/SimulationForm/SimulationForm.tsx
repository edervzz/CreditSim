interface Props {
  amount: string;
  rate: string;
  months: string;
  onChangeAmount: (amount: number) => void;
  onChangeRate: (rate: number) => void;
  onChangeMonths: (months: number) => void;
  onSubmit?: () => void;
}

export function SimulationForm({
  amount,
  rate,
  months,
  onChangeAmount,
  onChangeRate,
  onChangeMonths,
  onSubmit,
}: Props) {
  return (
    <div className="container" style={{ backgroundColor: "" }}>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit?.();
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
              value={amount}
              onChange={(e) => onChangeAmount(Number(e.target.value))}
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
              value={rate}
              onChange={(e) => onChangeRate(Number(e.target.value))}
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
              value={months}
              onChange={(e) => onChangeMonths(Number(e.target.value))}
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
