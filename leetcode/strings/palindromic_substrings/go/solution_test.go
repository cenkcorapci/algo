package palindromic_substrings

import "testing"

// Minimal test for the template implementation: only checks the empty
// string case so the stub remains passing. Add more tests once
// CountSubstrings is implemented.
func TestCountSubstrings_Empty(t *testing.T) {
    if got := CountSubstrings(""); got != 0 {
        t.Fatalf("CountSubstrings(\"\") = %d; want 0", got)
    }
}

