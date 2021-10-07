import "./App.css";
import React, { useState } from "react";
import ReactWordcloud from "react-wordcloud";
import axios from "axios";

function App() {
  const [words, setWords] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = React.useCallback(
    (evt) => {
      evt.preventDefault();
      setLoading(true);

      axios
        .get("http://localhost:5000/", { params: {  query: searchQuery } })
        .then((response) => {
          console.log("SUCCESS", response);
          setWords(response.data.words);
          setLoading(false);
        })
        .catch((error) => {
          console.log(error);
          setLoading(false);
        });
    },
    [searchQuery]
  );

  return (
    <div className="parent">
      <div className="container">
        <form>
          <input
            type="text"
            name="twitter handle"
            placeholder="Enter a Twitter handle to get started"
            value={searchQuery}
            onChange={(evt) => setSearchQuery(evt.target.value)}
          />
          <div className="buttonContainer">
            <button
              type="submit"
              onClick={handleSubmit}
              disabled={loading}
              name="search"
            >
              Search
            </button>
          </div>
        </form>
        <div className="wordcloud">
          {words && <ReactWordcloud words={words} />}
        </div>
      </div>
    </div>
  );
}

export default App;
