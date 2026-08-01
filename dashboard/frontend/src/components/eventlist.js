import React from 'react';
import { ListGroup, Badge } from 'react-bootstrap';

const EventList = ({ events }) => {
  if (events.length === 0) return <p>No events in selected date range.</p>;

  return (
    <ListGroup variant="flush" style={{ maxHeight: '400px', overflowY: 'auto' }}>
      {events.map(ev => (
        <ListGroup.Item key={ev.event_id}>
          <div className="d-flex justify-content-between">
            <span>
              <Badge bg={ev.impact_estimate === 'Very High' ? 'danger' : 'warning'} className="me-2">
                {ev.impact_estimate}
              </Badge>
              {ev.event_name}
            </span>
            <small className="text-muted">{new Date(ev.event_date).toLocaleDateString()}</small>
          </div>
          <small className="text-muted">{ev.region} - {ev.event_type}</small>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default EventList;
