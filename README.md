# latte-blogger

## Description

A toy project to use GitHub to manage the project (lightly), and use some GCP services that I've only used once or twice (serverless, managed API, datastore)

Ultimately I wanted to streamline the process of taking photos of latte art with my iPhone and have them viewable from a minimal website. A stretch goal would be to have some ML get trained on 'good' latte art and score the submissions?

Option A:
- An API, probably a serverless function for capturing the initial file POST, storing in some data store and kicking off a job for async processing of the image. A worker (serverless again?) process that would crop, tune, and resize for thumbs, etc. These images and the dirivitives of them would be stored in a bucket.

Option B:
- Same as A, but see if there's a trigger that can fire off a serverless function (or something) when a new image is added to a bucket. This would reduce the number of moving parts in that I wouldn't need a message queue.

## Backend

run `uvicorn backend.backend.main:app` from _this_ the root directory to fire up the API