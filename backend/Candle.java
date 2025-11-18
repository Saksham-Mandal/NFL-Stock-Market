/*
 * The open price of a candle will be equal to the previous candle's close.
 * The prices will be determined by fantasy points
*/
package backend;

public class Candle {
    private double open;
    private double close;

    public double getOpen(Candle candle) {
        return candle.open;
    }

    public double getClose(Candle candle) {
        return candle.close;
    }
}
