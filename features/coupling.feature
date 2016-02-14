Feature: Tolerance checking

    Scenario: Check 50H7g6
        Given I have 50H7g6 coupling
        Then diameter should be 50 milimiter
        # And hub's upper deviation should be 25.0 micrometer
        # And hub's lower deviation should be 0.0 micrometer
        # And hub's mid deviation should be 12.5 micrometer
        # And shaft's upper deviation should be -9.0 micrometer
        # And shaft's lower deviation should be -25.0 micrometer
        # And shaft's mid deviation should be -17.0 micrometer
        And max clearance should be 50.0 micrometer
        And min clearance should be 9.0 micrometer
        And mid clearance should be 29.5 micrometer
