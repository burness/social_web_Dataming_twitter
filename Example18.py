# Extracting Tweet entities from arbitrary text

# use a third-party package called twitter_text
import twitter_text

# Sample usage
txt="RT @SocialWebMining Mining 1M+ Tweets About #Syria http://wp.me/p3QiJd-1I"
ex=twitter_text.Extractor(txt)

print "Screen Names:",ex.extract_mentioned_screen_names_with_indices()
print "URLs:", ex.extract_urls_with_indices()
print "Hashtags:", ex.extract_hashtags_with_indices()