# VINYL SHUFFLE

[A simple app to provide a shuffle function for my collection of vinyl records.](https://charlieelwess-vinyl-shuffle-vinyl-shuffle-sl-v0-1-el4e3w.streamlit.app/)
![Vinyl Shuffle App Screenshot](vinyl_shuffle_sl_app_screenshot_v1.png)
I often find myself gravitating toward the same records, so I decided to make a shuffle app to make the decision for me.
In addition to my own purchases my collection comprises of at least two collections that were kindly donated to me.
Hopefully this app will help me explore the discs I've not yet heard.

I keep a record of my collection on Discogs, so I used the Discogs python client to retrieve its info from the API. Then it was simply a matter of making a collection CSV, selecting only the vinyl entries and randomly choosing one.

The app is implemented simply in Streamlit.

Unfortunately the app currently requires a jupyter notebook to update the collection data. This is because I had some trouble implementing the Discogs Client API authentication outside of this basic method. I'll work this out in future, and may try to add some augmentations like bio information, tracklisting, etc.
