import pytest


class TestBaseRepository:
    #  Tests that get_by_name with valid name returns expected document
    @pytest.mark.asyncio
    async def test_get_by_name_valid_name(self, base_repo):
        # Arrange
        name = 'test_name'
        document = {'name': name, 'value': 42}
        await base_repo.create(document)

        # Act
        result = await base_repo.get_by_name(name)

        # Assert
        assert result == document

    #  Tests that find with valid filter returns expected documents
    @pytest.mark.asyncio
    async def test_find_valid_filter(self, base_repo):
        # Arrange
        filter = {'value': 42}
        document1 = {'name': 'test_name1', 'value': 42}
        document2 = {'name': 'test_name2', 'value': 42}
        await base_repo.create(document1)
        await base_repo.create(document2)

        # Act
        result = [doc async for doc in base_repo.find(filter)]

        # Assert
        assert result == [document1, document2]

    #  Tests that create with valid document inserts document into collection
    @pytest.mark.asyncio
    async def test_create_valid_document(self, base_repo):
        # Arrange
        document = {'name': 'test_name', 'value': 42}

        # Act
        await base_repo.create(document)
        result = await base_repo.get_by_name('test_name')

        # Assert
        assert result == document

    #  Tests that update with valid filter and update updates document in collection
    @pytest.mark.asyncio
    async def test_update_valid_filter_and_update(self, base_repo):
        # Arrange
        filter = {'name': 'test_name'}
        document = {'name': 'test_name', 'value': 42}
        update = {'value': 43}
        await base_repo.create(document)

        # Act
        await base_repo.update(filter, update)
        result = await base_repo.get_by_name('test_name')
        result.pop('_id')

        # Assert
        assert result == {'name': 'test_name', 'value': 43}

    @pytest.mark.asyncio
    async def test_find_empty_filter(self, base_repo):
        # Arrange
        document = {'name': 'test_name', 'value': 42}
        await base_repo.create(document)
        # Act
        result = [doc async for doc in base_repo.find({})]

        # Assert
        assert result[0] == document
