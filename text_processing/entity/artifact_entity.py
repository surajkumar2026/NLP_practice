from dataclasses import dataclass

@dataclass
class ArtifactEntity:
    sentence_token: list[str]
    word_token: list[str]


@dataclass
class StemmingArtifactEntity:
    stemmed_words: list[str]
    