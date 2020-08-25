import React, { useState } from "react";
import { ActionBtn } from "./buttons";

export function ParentTweet(props) {
  const { tweet } = props;
  return tweet.parent ? (
    <div className="row">
      <div className="col-11 mx-auto p-3 border rounded">
        <p className="mb-0 text-muted small">Retweet</p>
        <Tweet hideActions className={" "} tweet={tweet.parent} />
      </div>
    </div>
  ) : null;
}

export function Tweet(props) {
  const { tweet, didRetweet, hideActions } = props;
  const [actionTweet, setActionTweet] = useState(
    props.tweet ? props.tweet : null
  );
  const className = props.className
    ? props.className
    : "col-10 mx-auto col-md-6";

  const handlePerfomAction = (newActionTweet, status) => {
    if (status === 200) {
      setActionTweet(newActionTweet);
    } else if (status === 201) {
      if (didRetweet) {
        didRetweet(newActionTweet);
      }
      // let the tweet list know.
    }
  };

  return (
    <div className={className}>
      <div>
        <p>
          {tweet.id} - {tweet.content}
        </p>
        <ParentTweet tweet={tweet} />
      </div>

      {actionTweet && hideActions !== true && (
        <div className="btn btn-group">
          <ActionBtn
            tweet={actionTweet}
            didPerfomAction={handlePerfomAction}
            action={{ type: "like", display: "Like" }}
          />
          <ActionBtn
            tweet={actionTweet}
            didPerfomAction={handlePerfomAction}
            action={{ type: "unlike", display: "Unlike" }}
          />
          <ActionBtn
            tweet={actionTweet}
            didPerfomAction={handlePerfomAction}
            action={{ type: "retweet", display: "Retweet" }}
          />
        </div>
      )}
    </div>
  );
}
