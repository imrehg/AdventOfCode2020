This can be done even simpler, based on other people's solutions elsewhere,
that I've seen after submitting:

* no need for the `*8`, just translate F,L->0 and B,R->1 and decode the
  number as binary.
* can to the translation easier as eg.
  `seat.translate(str.maketrans("BFRL", "1010"))` and parse that as a
  binary numnber, neat...
