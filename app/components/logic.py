from scipy.stats import norm


class CalculatorLogic:
    @staticmethod
    def calculate_spt(statistical_power: float) -> float:
        """Calculates the Statistical Power Threshold

        Args:
            statistical_power (float): Statistical Power

        Returns:
            float: Statistical Power Threshold
        """
        return norm.ppf(statistical_power)

    @staticmethod
    def calculate_clt(confidence_level: float) -> float:
        """Calculates the Confidence Level Threshold

        Args:
            confidence_level (float): Confidence Level

        Returns:
            float: Confidence Level Threshold
        """
        return norm.ppf(1-(1-confidence_level)/2)

    @staticmethod
    def calculate_adc(baseline_conversion_rate: float, lift: float) -> float:
        """Calculates the Absolute Difference in Conversion Rate

        Args:
            baseline_conversion_rate (float): Baseline Conversion Rate
            lift (float): Lift

        Returns:
            float: Absolute Difference in Conversion Rate
        """
        return baseline_conversion_rate * lift

    @staticmethod
    def calculate_roa(baseline_conversion_rate: float, lift: float) -> float:
        """Calculates the Rate of Alternative

        Args:
            baseline_conversion_rate (float): Baseline Conversion Rate
            lift (float): Lift

        Returns:
            float: Rate of Alternative
        """
        return baseline_conversion_rate*(1+lift)
    
    @staticmethod
    def calculate_dnvto(daily_visitors: int, number_of_offers: int) -> int:
        """Calculates the Daily Number of Visitors to Offer

        Args:
            daily_visitors (int): Total Number of Daily Visitors
            number_of_offers (int): Number of Offers Including Control

        Returns:
            int: Daily Number of Visitors to Offer
        """
        return int(daily_visitors / number_of_offers)

    @staticmethod
    def calculate_sspo(baseline_conversion_rate: float, lift: float,
        confidence_level_threshold: float, statistical_power_threshold: float) -> int:
        numerator = 2*((
                baseline_conversion_rate*(1-baseline_conversion_rate)
                +(1+lift)*baseline_conversion_rate*(1-(1+lift)*baseline_conversion_rate)
                ))
    @staticmethod
    def calculate_dct(sample_size_per_offer: float, number_of_offers: int) -> int:
        """Calculates the Days to Complete Test

        Args:
            sample_size_per_offer (float): Sample size per offer
            number_of_offers (int): Daily number of visitors to offer

        Returns:
            int: Days to Complete Test
        """
        return int(sample_size_per_offer/number_of_offers)
    
    # @staticmethod
    # def calculate_

    def __init__(self, inputs: dict) -> None:
        self.inputs = inputs
        return None

    def calculate(self) -> dict:
        return None