import React, { useState } from 'react';
import { Form, Button, Card } from 'react-bootstrap';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const DashboardFilters = ({ onDateChange }) => {
  const [start, setStart] = useState(null);
  const [end, setEnd] = useState(null);

  const handleApply = () => {
    onDateChange(start, end);
  };

  const handleReset = () => {
    setStart(null);
    setEnd(null);
    onDateChange(null, null);
  };

  return (
    <Card>
      <Card.Body>
        <h5>Date Filter</h5>
        <Form>
          <Form.Group className="mb-2">
            <Form.Label>Start Date</Form.Label>
            <DatePicker
              selected={start}
              onChange={date => setStart(date)}
              selectsStart
              startDate={start}
              endDate={end}
              className="form-control"
              placeholderText="Select start date"
            />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>End Date</Form.Label>
            <DatePicker
              selected={end}
              onChange={date => setEnd(date)}
              selectsEnd
              startDate={start}
              endDate={end}
              minDate={start}
              className="form-control"
              placeholderText="Select end date"
            />
          </Form.Group>
          <Button variant="primary" onClick={handleApply} className="me-2">Apply</Button>
          <Button variant="secondary" onClick={handleReset}>Reset</Button>
        </Form>
      </Card.Body>
    </Card>
  );
};

export default DashboardFilters;
