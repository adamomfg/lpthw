formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# This line uses single and double quotes because you can only close a quote
# with a quote of the same count (single or double.) But, since %r prints
# up the raw character, it will use double quotes only if there is a
# single quote mark used in the middle of the text (or at least that's what
# the behavior seems to suggest.)
print formatter % (
  "I had this thing.",
  "That you could type up right,",
  "But it didn't sing.",
  "So I said goodnight."
  )
