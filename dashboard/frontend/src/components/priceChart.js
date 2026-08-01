import React from 'react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  ReferenceLine, ResponsiveContainer
} from 'recharts';

const PriceChart = ({ data, events }) => {
  // Format data for recharts
  const chartData = data.map(d => ({
    date: new Date(d.Date).getTime(),
    price: d.Price
  }));

  // For event markers
  const eventMarkers = events.map(ev => ({
    date: new Date(ev.event_date).getTime(),
    label: ev.event_name,
    color: ev.impact_estimate === 'High' || ev.impact_estimate === 'Very High' ? 'red' : 'orange'
  }));

  return (
    <ResponsiveContainer width="100%" height={500}>
      <LineChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 20 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis
          dataKey="date"
          tickFormatter={(tick) => new Date(tick).toLocaleDateString()}
          domain={['auto', 'auto']}
          type="number"
        />
        <YAxis domain={['auto', 'auto']} label={{ value: 'Price (USD)', angle: -90, position: 'insideLeft' }} />
        <Tooltip
          labelFormatter={(label) => new Date(label).toLocaleDateString()}
          formatter={(value) => $${value.toFixed(2)}}
        />
        <Legend />
        <Line type="monotone" dataKey="price" stroke="#2563eb" strokeWidth={2} dot={false} name="Brent Oil Price" />
        {eventMarkers.map((ev, idx) => (
          <ReferenceLine
            key={idx}
            x={ev.date}
            stroke={ev.color}
            strokeDasharray="3 3"
            label={{ value: ev.label, position: 'top', fill: ev.color }}
          />
        ))}
      </LineChart>
    </ResponsiveContainer>
  );
};

export default PriceChart;
