from dataclasses import dataclass

@dataclass
class Credentials:
    nid_auth: str
    nid_session: str

    def as_cookie(self) -> dict[str, str]:
        return {
            "NID_AUT": self.nid_auth,
            "NID_SES": self.nid_session
        }

__all__ = [
    Credentials
]