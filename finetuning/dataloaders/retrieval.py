from torch.utils.data import Dataset as TorchDataset

class RetrievalPairDataset(TorchDataset):
    def __init__(
        self,
        dataset,
        tokenizer,
        max_length: int = None,
        is_lower: bool = False,
    ):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.is_lower = is_lower
        if max_length is None or max_length <= 0:
            self.max_length = tokenizer.model_max_length
        else:
            self.max_length = max_length

    def __len__(self):
        return len(self.dataset)

    def _normalize(self, text: str) -> str:
        if text is None:
            return ""
        if self.is_lower:
            return text.replace("I", "ı").lower()
        return text

    def _tokenize(self, text: str):
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        tokenized = {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
        }
        if "token_type_ids" in encoding:
            tokenized["token_type_ids"] = encoding["token_type_ids"].squeeze(0)
        return tokenized

    def __getitem__(self, idx):
        row = self.dataset[idx]
        anchor = self._normalize(row["anchor"])
        positive = self._normalize(row["positive"])

        anchor_tok = self._tokenize(anchor)
        positive_tok = self._tokenize(positive)

        item = {
            "anchor_input_ids": anchor_tok["input_ids"],
            "anchor_attention_mask": anchor_tok["attention_mask"],
            "positive_input_ids": positive_tok["input_ids"],
            "positive_attention_mask": positive_tok["attention_mask"],
        }

        if "token_type_ids" in anchor_tok:
            item["anchor_token_type_ids"] = anchor_tok["token_type_ids"]
        if "token_type_ids" in positive_tok:
            item["positive_token_type_ids"] = positive_tok["token_type_ids"]

        return item