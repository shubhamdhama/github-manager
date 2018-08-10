# Using GitHub APIs in Python using `requests`

## Introduction

This repo is created to explore GitHub APIs without using any API client.
The main purpose of this was to get the list of PRs I've created during the
whole GSoC period, but soon I may try other APIs as well and so I've
created this sample repo for all such examples.

## Instruction

Following environment variable needs to be set:

- `$TEMP_FILE`, which refers to a temporary file.

## Some curl commands to use some APIs from the terminal

Basic command line examples from GH API overview page.

```bash
curl https://api.github.com/zen

curl https://api.github.com/users/shubhamdhama

curl -i https://api.github.com/users/shubhamdhama

curl -i -u shubhamdhama -d '{"scopes": ["repo", "user"], "note": "getting-started"}' https://api.github.com/authorizations

curl -i -u shubhamdhama -H "X-GitHub-OTP:<OTP HERE>" -d '{"scopes": ["repo", "user"], "note": "getting-started"}'  https://api.github.com/authorizations

# Get your GitHub info including some data which isn't available publically
curl -H 'Authorization: token <TOKEN HERE>'  https://api.github.com/user
```
