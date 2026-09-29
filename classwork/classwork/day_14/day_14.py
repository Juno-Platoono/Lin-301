austen_opening = ["it", "is", "a", "truth", "universally", "acknowledged", "that", "a",
                   "single", "man", "in", "possession", "of", "a", "good", "fortune",
                   "must", "be", "in", "want", "of", "a", "wife"]

autsten_tokens = len(austen_opening)
austen_types = len(set(austen_opening))

austen_ttr=austen_types/autsten_tokens
print("austen trr: ", austen_ttr )


bronte_opening = ["there", "was", "no", "possibility", "of", "taking", "a", "walk",
                   "that", "day", "we", "had", "been", "wandering", "in", "the",
                   "leafless", "shrubbery", "an", "hour", "in", "the", "morning"]

bronte_tokens = len(bronte_opening)
bronte_types = len(set(bronte_opening))

bronte_ttr=bronte_types/bronte_tokens
print("bronte trr: ", bronte_ttr )

austen_words = set(austen_opening)
bronte_words=set(bronte_opening)

shared_words = austen_words & bronte_words
austen_only = austen_words - bronte_words

print("shared:",shared_words)
print("austen only:", austen_only)
