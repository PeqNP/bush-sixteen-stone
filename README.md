# Bush Sixteen Stone

This is a very simple algorithm meant to decode the binary code message on Bush's Sixteen Stone album.

So far as I can tell it's complete gibberish. The settings that produced the best results were setting the bit size to 7 bits (most ASCII is represented with only 7 bits).

Things I have tried:
- Concatenated the entire string (top to bottom) and read forwards and backwards.
- Changed bit sizes from 6-8, 7 producing the best results.

Some things that could be tried:
- Match all of the bits to respective ASCII characters and see if any patterns emerge. Essentially, find a match, take the match out, and then attempt to match the next set until all bits have been read.
- Concatenating the rows in a random order.

## Observations
The cover consists of 18 rows, 13 bits in each row making a total of 234 bits. The only number that divides equally, that would have any hope of producing a legible result, is 6.

The range of legible characters, in the ASCII table, are 32 ('space') to 127, but probably they only used up to 122 (little 'z'). This would then require at least 7 bits to get the whole range. 6 bits only provides characters up to 63, which means that only numbers would be available.

Many of the numbers are either not shown, obscured or illegible. The algorithm replaces all of these instances with either '0' or '1'. There are enough good bits, within the overall range, to produce _something_, if anything was there.
