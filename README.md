This is a website built using Django to do the following:
 - shorten a URL (similar to goo.gl)
 - track the times a user uses each shortened URL
 - provide a restful API

There are still some bugs to be worked out, but the underlying code is here.


# URLy Bird API

## Description

Add a REST-based API to [URLy Bird](https://github.com/tiy-gvl-python/urly-bird-lite).

## Objectives

### Learning Objectives

After completing this assignment, you should be able to:

* Design a simple REST API.
* Implement authentication and authorization for an API in Django.

## Details

### Deliverables

Instead of forking this repo, use your previous URLy Bird project and push there.

## Normal Mode

Add an API under the URL `/api` to URLy Bird.

This API should be read-only unless the user is authenticated. If authenticated,
the user can add new bookmarks and edit and delete their own bookmarks.

The API should allow for:

* Viewing, editing, and deleting bookmarks
* Seeing the click stats for a bookmark
* Adding a click to a bookmark
* Allowing a user to see their overall stats (This is a replication of the
  overall stats page from the original assignment.)

## Hard Mode

For hard mode, do everything shown above, plus any of the following features.

* Allow new user creation through the API.
* Allow token-based authentication.
* Support topical lists or tags from the original assignment through the API.
* Add functional tests for your API.
