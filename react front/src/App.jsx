import { useState } from 'react'
import './App.css'

const API_URL = 'http://127.0.0.1:8000'

const App = () => {
  const [principle, setPrinciple] = useState('')
  const [rate, setRate] = useState('')
  const [time, setTime] = useState('')
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleCalculate = async (e) => {
    e.preventDefault()
    setError('')
    setResult(null)
    setLoading(true)

    try {
      const params = new URLSearchParams({
        principle: principle,
        r: rate,
        n: time,
      })

      const response = await fetch(`${API_URL}/interest?${params}`)
      const data = await response.json()

      if (!data.isSucess) {
        setError(data.message || 'Calculation failed')
        return
      }

      setResult(data)
    } catch {
      setError('Backend se connect nahi ho paya. Pehle backend run karein: uvicorn main:app --reload')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <h1>Simple Interest Calculator</h1>
      <p className="subtitle">React + FastAPI</p>

      <form className="calculator-form" onSubmit={handleCalculate}>
        <label>
          Principle (₹)
          <input
            type="number"
            value={principle}
            onChange={(e) => setPrinciple(e.target.value)}
            placeholder="e.g. 6500000"
            required
            min="1"
          />
        </label>

        <label>
          Rate of Interest (%)
          <input
            type="number"
            value={rate}
            onChange={(e) => setRate(e.target.value)}
            placeholder="e.g. 8"
            required
            min="1"
          />
        </label>

        <label>
          Time (years)
          <input
            type="number"
            value={time}
            onChange={(e) => setTime(e.target.value)}
            placeholder="e.g. 10"
            required
            min="1"
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? 'Calculating...' : 'Calculate'}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <h2>Result</h2>
          <p><span>Principle:</span> ₹{result.principle.toLocaleString('en-IN')}</p>
          <p><span>Simple Interest:</span> ₹{result.si.toLocaleString('en-IN')}</p>
          <p><span>Total Payment:</span> ₹{result.totalPayment.toLocaleString('en-IN')}</p>
        </div>
      )}
    </div>
  )
}

export default App
