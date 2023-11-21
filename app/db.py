from motor.motor_asyncio import AsyncIOMotorClient


class MongoManager:
    def __init__(
            self,
            host: str = "localhost",
            port: int = 27017,
            db: str = "default"
            ) -> None:
        self.client = AsyncIOMotorClient(
            host,
            port
        )
        self.db = self.client[db]
        self.forms = self.db.forms

    async def get_templates(self, filter: dict = {}) -> list:
        """_summary_ Return templates by filter

        Args:
            filter (dict, optional): some filter like {"field1": "field1_type"}
            Defaults to {}.

        Returns:
            list: list of entrys by filter
        """
        result = []
        async for doc in self.forms.find(filter):
            del doc["_id"]
            result.append(doc)
        return result

    async def create_template(self, fields: dict) -> bool:
        """_summary_ Creates template entry in Mongo

        Args:
            fields (dict): filter like {"field1": "field1_type"}

        Raises:
            ValueError: if template already exists
        """
        form = await self.forms.find_one(fields)
        if form:
            raise ValueError("template is already exists")
        await self.forms.insert_one(fields)
        return True
