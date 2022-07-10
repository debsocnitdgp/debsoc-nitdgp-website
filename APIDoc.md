# API Documentation

The following API endpoints are provided by the project:

## List All Members:

Endpoint: `/main/api/members`

Input: `none`

Return format:

```json
{
  "2": [
    // Members of second year
    {
      // Every member returned by the API follows the followinf format
      "id": 1, // Int
      "username": "", // String
      "firstname": "", // String
      "lastname": "", // String
      "email": "", // String
      "bio": "", // String
      "year": "Second", // String
      "post": "Senior Member", // String
      "sno": null, // Int or null
      "dp": null, // Url or null
      "facebook_url": null, // Url or null
      "instagram_url": null, // Url or null
      "linkedin_url": null // Url or null
    }
  ],
  "3": [
    /** Members of pre-final year */
  ],
  "4": [
    /** Members of final year */
  ]
}
```

## List All Events

Endpoint: `/main/api/events`

Input: `none`

Return format:

```json
{
  "all": [
    {
      // All events follow the following structure
      "id": 6, // Int
      "event_name": "", // String
      "event_description": "", // String
      "poster": null, // Url or null
      "event_datetime": "2022-06-09T17:21:04+05:30", // Datetime
      "event_mode": "Online", // String
      "event_starttime": "2022-06-07T17:12:58+05:30", // Datetime
      "event_endtime": "2022-06-08T17:12:58+05:30", // Datetime
      "active": true, // Boolean
      "text1": "", // String
      "url1": "", // String
      "text2": "", // String
      "url2": "", // String
      "text3": "", // String
      "url3": "" // String
    }
  ],
  "upcoming": [],
  "live": []
}
```

## List one event

Endpoint: `/main/api/event/<int:event_id>`

Input: `event_id: int`: Id of the event

Return format:

```json
{
  "id": 6, // Int
  "event_name": "", // String
  "event_description": "", // String
  "poster": null, // Url or null
  "event_datetime": "2022-06-09T17:21:04+05:30", // Datetime
  "event_mode": "Online", // String
  "event_starttime": "2022-06-07T17:12:58+05:30", // Datetime
  "event_endtime": "2022-06-08T17:12:58+05:30", // Datetime
  "active": true, // Boolean
  "text1": "", // String
  "url1": "", // String
  "text2": "", // String
  "url2": "", // String
  "text3": "", // String
  "url3": "" // String
}
```

## List all Alumnis

Endpoint: `/main/api/alumni`

Input: None

Return format:

```json
{
  "2016": [
    {
      // All alumni objects follow the following strucutre
      "id": 4, // Int
      "firstname": "", // String
      "lastname": "", // String
      "email": "", // String
      "batch": "2016", // String
      "sno": null, // Int or null
      "propic": null, // URL or null
      "facebook_url": null, // URL or null
      "instagram_url": null, // URL or null
      "linkedin_url": null // URL or null
    }
  ],
  "2017": [],
  "2018": []
  // ....
}
```

## List All Blogs

Endpoint: `/main/api/blogs`

Input: `none`

Return format:

```json
[
  {
    "id": 1,
    "title": "", // String
    "blog_text": "", // String
    "image_url": null, // URL or null
    "created_on": "2022-06-10T21:44:22.790198+05:30", // Datetime
    "active": true, // Boolean
    "author": "" // String
  }
  //...
]
```

## List one blog

Endpoint: `/main/api/blog/<int:blog_id>`

Input: `blog_id: int`: ID of the blog



Return format:

```json
{
  "id": 1,
  "title": "", // String
  "blog_text": "", // String
  "image_url": null, // URL or null
  "created_on": "2022-06-10T21:44:22.790198+05:30", // Datetime
  "active": true, // Boolean
  "author": "" // String
}
```

## Get comments on a blog

Endpoint: `/main/api/comments/<blog_id:int>`

Input: `blog_id:int`: ID of the blog whose comments are needed.

Return format:

```json
[
  {
    "id": 2, // Int
    "comment_by": "",  // String
    "comment": "",  // String
    "commented_on": "2022-06-10T21:44:10.573409+05:30",  // Datetime
    "active": true, // Boolean
    "post": 1 // Int
  },
  {
    "id": 1,
    "comment_by": "vnjjehvr",
    "comment": "hsdetvhg",
    "commented_on": "2022-06-10T21:44:10.573105+05:30",
    "active": true,
    "post": 1
  },
  // ...
]
```