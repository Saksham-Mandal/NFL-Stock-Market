type ChartNavProps = {
  selectedRange: string;
  onSelectRange: (range: string) => void;
};

const ranges = ["1D", "1W", "1M", "3M", "1Y", "ALL"];

const ChartNav = ({ selectedRange, onSelectRange }: ChartNavProps) => {
  return (
    <div className="chart-nav">
      {ranges.map((range) => (
        <button
          key={range}
          className={`chart-nav-btn ${selectedRange === range ? "active" : ""}`}
          onClick={() => onSelectRange(range)}
        >
          {range}
        </button>
      ))}
    </div>
  );
};

export default ChartNav;
