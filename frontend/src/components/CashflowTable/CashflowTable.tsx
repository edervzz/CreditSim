import type { PaymentModel } from "../../domain";

interface Props {
  cashflow?: PaymentModel[];
}
export function CashflowTable({ cashflow }: Props) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Interest</th>
          <th scope="col">Principal</th>
          <th scope="col">Quota</th>
          <th scope="col">Outstanding</th>
        </tr>
      </thead>
      <tbody>
        {cashflow?.map((x) => (
          <tr id={x.month.toString()}>
            <td>{x.month}</td>
            <td>{x.interest}</td>
            <td>{x.principal}</td>
            <td>{x.quota}</td>
            <td>{x.outstanding}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
