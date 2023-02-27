from scipy.stats import norm
from math import ceil


class CalculatorLogic:
    @staticmethod
    def spt(statistical_power: float) -> float:
        """Calculates the Statistical Power Threshold

        Args:
            statistical_power (float): Statistical Power

        Returns:
            float: Statistical Power Threshold
        """
        return round(norm.ppf(statistical_power),4)

    @staticmethod
    def clt(confidence_level: float) -> float:
        """Calculates the Confidence Level Threshold

        Args:
            confidence_level (float): Confidence Level

        Returns:
            float: Confidence Level Threshold
        """
        return round(norm.ppf(1-(1-confidence_level)/2),4)

    @staticmethod
    def adc(baseline_conversion_rate: float, lift: float) -> float:
        """Calculates the Absolute Difference in Conversion Rate

        Args:
            baseline_conversion_rate (float): Baseline Conversion Rate
            lift (float): Lift

        Returns:
            float: Absolute Difference in Conversion Rate
        """
        return round(baseline_conversion_rate * lift,4)

    @staticmethod
    def roa(baseline_conversion_rate: float, lift: float) -> float:
        """Calculates the Rate of Alternative

        Args:
            baseline_conversion_rate (float): Baseline Conversion Rate
            lift (float): Lift

        Returns:
            float: Rate of Alternative
        """
        return round(baseline_conversion_rate*(1+lift),4)
    
    @staticmethod
    def dnvto(daily_visitors: int, number_of_offers: int) -> int:
        """Calculates the Daily Number of Visitors to Offer

        Args:
            daily_visitors (int): Total Number of Daily Visitors
            number_of_offers (int): Number of Offers Including Control

        Returns:
            int: Daily Number of Visitors to Offer
        """
        return ceil(daily_visitors / number_of_offers)

    @staticmethod
    def sspov(baseline_conversion_rate: float, lift: float,
        confidence_level_threshold: float, statistical_power_threshold: float) -> int:
        """Calculates the Sample Size per Offer (# of visitors)

        Args:
            baseline_conversion_rate (float): Baseline conversion rate
            lift (float): Lift
            confidence_level_threshold (float): Confidence level threshold
            statistical_power_threshold (float): Statistical power threshold

        Returns:
            int: Sample Size per Offer (# of visitors)
        """
        numerator = 2*((
                baseline_conversion_rate*(1-baseline_conversion_rate)
                +(1+lift)*baseline_conversion_rate*(1-(1+lift)*baseline_conversion_rate)
                )/2)*(confidence_level_threshold + statistical_power_threshold)**2
        denominator = (baseline_conversion_rate - baseline_conversion_rate*(1+lift))**2
        return int(numerator/denominator)

    @staticmethod
    def sspoc(baseline_conversion_rate: float, sample_size_per_offer: int) -> int:
        """Calculates the Sample Size per Offer (# of conversions)

        Args:
            baseline_conversion_rate (float): Baseline conversion rate
            sample_size_per_offer (int): Sample size per offer (# of visitors)

        Returns:
            int: Sample Size per Offer (# of conversions)
        """
        return int(baseline_conversion_rate*sample_size_per_offer)
        
    @staticmethod
    def dct(sample_size_per_offer: int, number_of_offers: int) -> int:
        """Calculates the Days to Complete Test

        Args:
            sample_size_per_offer (int): Sample size per offer
            number_of_offers (int): Daily number of visitors to offer

        Returns:
            int: Days to Complete Test
        """
        return ceil(sample_size_per_offer/number_of_offers)
    
    @staticmethod
    def wct(days_to_complete_test: int) -> int:
        """Calculates the weeks to complete test

        Args:
            days_to_complete_test (int): Days to Complete Test

        Returns:
            int: Weeks to complete test
        """
        return ceil(days_to_complete_test/7)

    def __init__(self, inputs: dict) -> None:
        self.inputs = inputs
        statistical_power = inputs.get('statistical_power')
        confidence_level = inputs.get('confidence_level')
        baseline_conversion_rate = inputs.get('baseline_conversion_rate')
        lift = inputs.get('lift')
        daily_visitors = inputs.get('daily_visitors')
        number_of_offers = inputs.get('number_of_offers')
        
        self.outputs = dict()

        self.outputs["statistical_power_threshold"] = self.spt(statistical_power)
        self.outputs["confidence_level_threashold"] = self.clt(confidence_level)
        self.outputs["absolute_difference_conversion_rate"] = self.adc(baseline_conversion_rate, lift)
        self.outputs["rate_alternative"] = self.roa(baseline_conversion_rate, lift)
        self.outputs["daily_number_visitors_offer"] = self.dnvto(daily_visitors, number_of_offers)
        self.outputs["sample_size_offer_visitors"] = self.sspov(
            baseline_conversion_rate, lift, 
            self.outputs["confidence_level_threashold"], 
            self.outputs["statistical_power_threshold"])

        self.outputs["sample_size_offer_conversion"] = self.sspoc(
            baseline_conversion_rate,
            self.outputs["sample_size_offer_visitors"])

        self.outputs["days_to_complete_test"] = self.dct(
            self.outputs["sample_size_offer_visitors"], 
            self.outputs["daily_number_visitors_offer"])
        return None