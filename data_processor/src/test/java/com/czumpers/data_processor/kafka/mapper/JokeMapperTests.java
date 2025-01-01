package com.czumpers.data_processor.kafka.mapper;

import com.czumpers.data_processor.kafka.model.OnePartJokeConsumed;
import com.czumpers.data_processor.kafka.model.ResourceProduced;
import com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class JokeMapperTests {

    private OnePartJokeMapper onePartJokeMapper;
    private TwoPartJokeMapper twoPartJokeMapper;

    @BeforeEach
    void setUp() {
        onePartJokeMapper = new OnePartJokeMapper();
        twoPartJokeMapper = new TwoPartJokeMapper();
    }

    @Test
    void testOnePartJokeMapper() {
        OnePartJokeConsumed joke = new OnePartJokeConsumed();
        joke.setId(1);
        joke.setType("one-part");
        joke.setCategory("funny");
        joke.setFlags(Map.of("nsfw", false, "religious", true));
        joke.setJoke("Why don't scientists trust atoms? Because they make up everything.");

        ResourceProduced result = onePartJokeMapper.mapToResource(joke);

        assertEquals("joke", result.getType());
        assertEquals("one part jokes", result.getSource());
        assertEquals("Why don't scientists trust atoms? Because they make up everything.", result.getContent());
        assertTrue(result.getTags().contains("funny"));
        assertTrue(result.getTags().contains("god"));
        assertFalse(result.getTags().contains("explicit content"));
        assertNotNull(result.getPublished());
    }

    @Test
    void testTwoPartJokeMapper() {
        TwoPartJokeConsumed joke = new TwoPartJokeConsumed();
        joke.setId(2);
        joke.setType("two-part");
        joke.setCategory("hilarious");
        joke.setFlags(Map.of("sexist", true, "racist", false));
        joke.setSetup("Why did the chicken cross the road?");
        joke.setDelivery("To get to the other side!");

        ResourceProduced result = twoPartJokeMapper.mapToResource(joke);

        assertEquals("joke", result.getType());
        assertEquals("two part jokes", result.getSource());
        assertEquals("Why did the chicken cross the road?\nTo get to the other side!", result.getContent());
        assertTrue(result.getTags().contains("hilarious"));
        assertTrue(result.getTags().contains("gender inequality")); // sexist tag
        assertFalse(result.getTags().contains("racism jokes"));
        assertNotNull(result.getPublished());
    }

    @Test
    void testEmptyFlags() {
        OnePartJokeConsumed joke = new OnePartJokeConsumed();
        joke.setFlags(Map.of());
        joke.setCategory("random");
        joke.setJoke("Just a random joke.");

        ResourceProduced result = onePartJokeMapper.mapToResource(joke);

        assertEquals("joke", result.getType());
        assertEquals("one part jokes", result.getSource());
        assertEquals("Just a random joke.", result.getContent());
        assertTrue(result.getTags().contains("random"));
        assertNotNull(result.getPublished());
    }

    @Test
    void testNoCategory() {
        TwoPartJokeConsumed joke = new TwoPartJokeConsumed();
        joke.setFlags(Map.of("explicit", true));
        joke.setSetup("Setup?");
        joke.setDelivery("Delivery!");

        ResourceProduced result = twoPartJokeMapper.mapToResource(joke);

        assertEquals("joke", result.getType());
        assertEquals("two part jokes", result.getSource());
        assertEquals("Setup?\nDelivery!", result.getContent());
        assertTrue(result.getTags().contains("adult")); // explicit tag
        assertNotNull(result.getPublished());
    }
}
