import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PriceChart from './components/PriceChart';
import EventList from './components/EventList';
import DashboardFilters from './components/DashboardFilters';
import { Container, Row, Col, Card } from 'react-bootstrap';

function App() {
  const [priceData, setPriceData] = useState([]);
  const [events, setEvents] = useState([]);
  const [filteredEvents, setFilteredEvents] = useState([]);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from API
    const fetchData = async () => {
      try {
        const [priceRes, eventRes] = await Promise.all([
          axios.get('/api/prices/'),
          axios.get('/api/events/')
        ]);
        setPriceData(priceRes.data.data);
        setEvents(eventRes.data.events);
        setFilteredEvents(eventRes.data.events);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    // Filter events by date range
    if (startDate && endDate) {
      const filtered = events.filter(ev => {
        const d = new Date(ev.event_date);
        return d >= startDate && d <= endDate;
      });
      setFilteredEvents(filtered);
    } else {
      setFilteredEvents(events);
    }
  }, [startDate, endDate, events]);

  const handleDateChange = (start, end) => {
    setStartDate(start);
    setEndDate(end);
  };

  if (loading) return <div className="text-center mt-5">Loading dashboard...</div>;

  return (
    <Container fluid className="p-4">
      <h1 className="mb-4">Brent Oil Price Change Point Analysis</h1>
      <Row>
        <Col md={3}>
          <DashboardFilters onDateChange={handleDateChange} />
          <Card className="mt-3">
            <Card.Body>
              <h5>Events</h5>
              <EventList events={filteredEvents} />
            </Card.Body>
          </Card>
        </Col>
        <Col md={9}>
          <Card>
            <Card.Body>
              <PriceChart data={priceData} events={filteredEvents} />
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
