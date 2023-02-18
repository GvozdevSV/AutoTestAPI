from  pydantic import BaseModel, validator


class Post(BaseModel):
    id: int
    title: str
    @validator("id")
    def check_that_id_less_then_two(cls, v):
        if v > 2:
            raise ValueError('id is not less two')
        else:
            return v

    ## [{'id': 1, 'title': 'Post 1'},