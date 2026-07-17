from address import Address

class Mailing:

    def _init_ (self, to_address: Address, from_address: Address,  cost, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

