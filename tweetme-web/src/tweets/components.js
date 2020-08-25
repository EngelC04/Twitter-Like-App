import React, { useState } from "react";
import { TweetsList } from "./list";
import { apiTweetCreate } from "./lookup";

function TweetCreate(props) {
  const textAreaRef = React.createRef();
  const { didTweet } = props;
  const handleBackendUpdate = (response, status) => {
    if (status === 201) {
      didTweet(response);
    } else {
      console.log(response);
      alert("An Error occured please try again");
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const newVal = textAreaRef.current.value;
    // backend api request
    apiTweetCreate(newVal, handleBackendUpdate);

    textAreaRef.current.value = "";
  };

  return (
    <div className={props.className}>
      <form onSubmit={handleSubmit}>
        <textarea
          ref={textAreaRef}
          required={true}
          className="form-control"
          name="tweet"
        ></textarea>
        <button type="submit" className="btn btn-primary my-3">
          Tweet
        </button>
      </form>
    </div>
  );
}

export function TweetsComponent(props) {
  const [newTweets, setNewTweets] = useState([]);
  const canTweet = props.canTweet === "false" ? false : true;
  const handleNewTweet = (newTweet) => {
    // backend api response handler
    let tempNewTweets = [...newTweets];
    tempNewTweets.unshift(newTweet);
    setNewTweets(tempNewTweets);
  };

  return (
    <div className={props.className}>
      {canTweet === true && (
        <TweetCreate didTweet={handleNewTweet} className="col-12 mb-3" />
      )}
      <TweetsList newTweets={newTweets} {...props} />
    </div>
  );
}
