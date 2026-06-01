import { useEffect, useRef } from "react";
import {
  createChart,
  CandlestickSeries,
  ColorType,
  type Time,
} from "lightweight-charts";
import type { Candle } from "../util/types";

/*
const sampleData = [
  { time: "2026-04-01", open: 100, high: 108, low: 97, close: 105 },
  { time: "2026-04-02", open: 105, high: 110, low: 101, close: 103 },
  { time: "2026-04-03", open: 103, high: 112, low: 102, close: 109 },
  { time: "2026-04-04", open: 109, high: 115, low: 106, close: 111 },
  { time: "2026-04-05", open: 111, high: 113, low: 104, close: 106 },
  { time: "2026-04-06", open: 106, high: 118, low: 105, close: 116 },
  { time: "2026-04-07", open: 116, high: 120, low: 112, close: 114 },
  { time: "2026-04-08", open: 114, high: 121, low: 113, close: 119 },
];
*/

type ChartProps = {
  candles: Candle[];
};

const PlayerChart = ({ candles }: ChartProps) => {
  const chartContainerRef = useRef<HTMLDivElement | null>(null);
  const chartRef = useRef<any>(null);
  const seriesRef = useRef<any>(null);

  //create chart once
  useEffect(() => {
    if (!chartContainerRef.current) return;

    const chart = createChart(chartContainerRef.current, {
      width: chartContainerRef.current.clientWidth,
      height: 400,
      layout: {
        background: { type: ColorType.Solid, color: "#0a0f1c" },
        textColor: "#e5e7eb",
      },
      grid: {
        vertLines: { color: "#1e293b" },
        horzLines: { color: "#1e293b" },
      },
      rightPriceScale: {
        borderColor: "#334155",
      },
      timeScale: {
        borderColor: "#334155",
      },
    });

    const candleSeries = chart.addSeries(CandlestickSeries, {
      upColor: "#22c55e",
      downColor: "#ef4444",
      borderVisible: false,
      wickUpColor: "#22c55e",
      wickDownColor: "#ef4444",
    });

    const chartData = candles.map((c: any) => ({
      time: Number(c.time.replace("-W", "")) as Time, // "2024-W3" → 20243
      open: c.open,
      high: c.high,
      low: c.low,
      close: c.close,
    }));

    candleSeries.setData(chartData);
    chart.timeScale().fitContent();

    const handleResize = () => {
      if (!chartContainerRef.current) return;
      chart.applyOptions({
        width: chartContainerRef.current.clientWidth,
      });
    };

    window.addEventListener("resize", handleResize);

    chartRef.current = chart;
    seriesRef.current = candleSeries;

    return () => {
      window.removeEventListener("resize", handleResize);
      chart.remove();
    };
  }, []);

  //updates chart whenever new player is chosen
  useEffect(() => {
    if (!seriesRef.current || !chartRef.current) return;

    const chartData = candles.map((c) => ({
      time: c.time, // "2024-W3" → 20243
      open: c.open,
      high: c.high,
      low: c.low,
      close: c.close,
    }));

    console.log("Updating chart with:", chartData);

    seriesRef.current.setData(chartData);
    chartRef.current.timeScale().fitContent();
  }, [candles]);

  return (
    <>
      <div className="chart-card">
        <div className="chart-inner">
          <div ref={chartContainerRef} />
        </div>
      </div>
    </>
  );
};

export default PlayerChart;
