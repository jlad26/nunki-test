### Connection management
- Need to handle what happens if connection drops? Automatic retry?

### Dockerization
- Why is calling as a module necessary? Answer - it's not necessary, but if we use are using Flask we need to set the host to 0.0.0.0. That can be done by running flask as a module with option `--host=0.0.0.0`. Alternatively we can run as a script but we need to use `app.run(host=0.0.0.0)`.
- When calling as a module, why is the `connection` variable not available to module when it is defined within `if __name__ == '__main__':`? Answer: Because it is called as module nothing within `if __name__ == '__main__':` is executed. `app.run(Debug=True)` wasn't being executed either - the app was being run using `flask run --host=0.0.0.0` as a `python3` command (see dockerfile)

### Caching
Is it useful to think about caching?
- At Twitter API level, to reduce volume of data / calls over internet? E.g. if last call was < x seconds ago, just use cached data? Does Twitter API have a way to e.g. get tweets only back to a certain time? (But problematic with possible deletion of tweets?)
- At app API level, to reduce use of local network? E.g. refuse request as too recent? (Requires that requester sends timestamp of last request, or API stores requesting IP address or requires user info)