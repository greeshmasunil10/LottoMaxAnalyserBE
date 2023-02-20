import React, { useState } from 'react';
import './App.css';

function App() {
  const [startYear, setStartYear] = useState('');
  const [endYear, setEndYear] = useState('');
  const [results, setResults] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isGraphEnlarged, setIsGraphEnlarged] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setIsLoading(true);
    const response = await fetch(`https://lottomax-analyser.herokuapp.com/analyser?start_year=${startYear}&end_year=${endYear}`, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log(`https://lottomax-analyser.herokuapp.com/analyser?start_year=${startYear}&end_year=${endYear}`)
    const data = await response.json();
    console.log("got data!!")
    console.log(data)
    // Decode the base64-encoded image data
    const numberFrequencyGraph = 'data:image/png;base64,' + data.numberFrequencyGraph;

    setResults(data);
    setIsLoading(false);
  };

  const handleDownloadClick = async (event) => {
    event.preventDefault();

    // Call the download API
    const response = await fetch(`https://lottomax-analyser.herokuapp.com/download`);
    const blob = await response.blob();
    const url = window.URL.createObjectURL(new Blob([blob]));

    // Create a link element and click it to download the file
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'DrawsDataWithDates.txt');
    document.body.appendChild(link);
    link.click();
  };

  const handleEnlargedImageClick = () => {
    setIsGraphEnlarged(!isGraphEnlarged);
  };
  
  return (
    <div className="container">
      <h1>Lotto Max Analyser</h1>

      <form onSubmit={handleSubmit}>
        <label htmlFor="start-year">Start Year:</label>
        <input type="number" id="start-year" name="start-year" required value={startYear} onChange={(event) => setStartYear(event.target.value)} />

        <label htmlFor="end-year">End Year:</label>
        <input type="number" id="end-year" name="end-year" required value={endYear} onChange={(event) => setEndYear(event.target.value)} />

        <button type="submit">Submit</button>
      </form>

      {isLoading && <p>Loading results...</p>}

      {results && (
        <div>
          <button onClick={handleDownloadClick}>Download all draws</button>
          <h2>Number Frequency Graph</h2>
          <img src={`data:image/png;base64, ${results.numberFrequencyGraph}`} alt="NumberFrequencyGraph"  className={isGraphEnlarged ? "enlarged" : ""} onClick={handleEnlargedImageClick}/>

          {/* <h2>Draws Graph</h2> */}
          <p style={{textAlign:"center"}}>Click on the image to enlarge.</p>
          {/* <img src={results.drawsGraph} alt="DrawsGraph" className={isGraphEnlarged ? "enlarged" : ""} onClick={handleEnlargedImageClick} /> */}
          {isGraphEnlarged && (
            <button onClick={handleEnlargedImageClick}>Close</button>
          )}

        </div>
      )}
    </div>
  );
}

export default App;
