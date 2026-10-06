class TransmissionLineSagCalculator:
    def __init__(self, span, conductor_weight, tension):
        self.span = span
        self.conductor_weight = conductor_weight
        self.tension = tension

    def calculate_sag(self):
        # Sag formula for level supports
        sag = (self.conductor_weight * self.span ** 2) / (
            8 * self.tension
        )

        return sag

    def calculate_clearance(self):
        sag = self.calculate_sag()

        # Lowest point of conductor from support level
        clearance_drop = sag

        return clearance_drop

    def display_result(self):
        sag = self.calculate_sag()

        print("\n----- TRANSMISSION LINE SAG CALCULATOR -----")

        print(f"Span Length        : {self.span:.2f} m")
        print(f"Conductor Weight   : {self.conductor_weight:.3f} N/m")
        print(f"Conductor Tension  : {self.tension:.2f} N")

        print(f"\nCalculated Sag     : {sag:.3f} m")

        if sag < 1:
            print("Sag Status         : LOW")
        elif sag <= 3:
            print("Sag Status         : NORMAL")
        else:
            print("Sag Status         : HIGH")

        print(
            f"\nThe conductor sags approximately "
            f"{sag:.3f} m at the lowest point."
        )


def main():

    print("==============================================")
    print("       TRANSMISSION LINE SAG CALCULATOR")
    print("==============================================")

    try:
        span = float(
            input("\nEnter span length (m): ")
        )

        conductor_weight = float(
            input("Enter conductor weight (N/m): ")
        )

        tension = float(
            input("Enter conductor tension (N): ")
        )

        if span <= 0 or conductor_weight <= 0 or tension <= 0:
            print("\nPlease enter positive values.")
            return

        calculator = TransmissionLineSagCalculator(
            span,
            conductor_weight,
            tension
        )

        calculator.display_result()

    except ValueError:
        print("\nInvalid input! Please enter numerical values.")


if __name__ == "__main__":
    main()
